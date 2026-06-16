class Vector:
    def __init__(self,vector):
        self.vector = vector

    def __add__(self, other):
        return Vector([a + b for a,b in zip(self.vector,other.vector)])

    def __sub__(self, other):
        return Vector([a - b for a,b in zip(self.vector,other.vector)])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def magnitude(self):
        return sum([a**2 for a in self.vector]) ** 0.5

    def normalize(self):
        magnitude = self.magnitude()
        return Vector([a/magnitude for a in  self.vector])

    def cosine_similarity(self,other):
        return self.dot(other)/(self.magnitude() * other.magnitude())


a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

print(f"a + b = {(a + b).vector}")
print(f"a · b = {a.dot(b)}")
print(f"|a| = {a.magnitude():.4f}")
print(f"cosine similarity = {a.cosine_similarity(b):.4f}")


class Matrix:
    def __init__(self,rows):
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))


    def __matmul__(self, other):
        if isinstance(other,Vector):
            result = []
            for i in range(self.shape[0]):
                value = sum(a * b for a, b in zip(self.rows[i], other.vector))
                result.append(value)
            return Vector(result)
        rows = []
        for i in range(self.shape[0]):
            row = []
            for j in range(other.shape[1]):
                value = sum(self.rows[i][k] * other.rows[k][j] for k in range(self.shape[1]))
                row.append(value)
            rows.append(row)
        return Matrix(rows)

    def transpose(self):
        new_rows = []
        for i in range(self.shape[1]):
            new_row = []
            for j in range(self.shape[0]):
                new_row.append(self.rows[j][i])
            new_rows.append(new_row)
        return Matrix(new_rows)

rotation_90 = Matrix([[0, -1], [1, 0]])
point = Vector([3, 1])
rotated = rotation_90 @ point
print(f"Original: {point.vector}")
print(f"Rotated 90°: {rotated.vector}")
M = Matrix([[1, 2, 3], [4, 5, 6]])
print(f"Original shape: {M.shape}")
print(f"Transposed shape: {M.transpose().shape}")
print(f"Transposed: {M.transpose().rows}")


def is_linearly_independent(vectors):
    n = len(vectors)
    dim = len(vectors[0].vector)

    rows = [v.vector[:] for v in vectors]

    rank = 0

    for col in range(dim):
        # find pivot
        pivot = None
        for row in range(rank, len(rows)):
            if abs(rows[row][col]) > 1e-10:
                pivot = row
                break

        if pivot is None:
            continue

        # swap pivot row to rank position
        rows[rank], rows[pivot] = rows[pivot], rows[rank]

        # scale pivot row to 1
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]

        # eliminate this column from all other rows
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col]
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]

        rank += 1

    return rank == n

def project(a, b):
    scalar = a.dot(b) / b.dot(b)
    return Vector([scalar * x for x in b. vector])


def gram_schmidt(vectors):
    orthonormal = []
    for v in vectors:
        w = v
        for u in orthonormal:
            proj = project(w, u)
            w = w - proj
        if w.magnitude() < 1e-10:
            continue
        orthonormal.append(w.normalize())
    return orthonormal

v1 = Vector([1, 0, 0])
v2 = Vector([0, 1, 0])
v3 = Vector([2, 1, 0])

print(is_linearly_independent([v1, v2, v3]))
print(is_linearly_independent([v1, v2]))
v1 = Vector([1, 0, 0])
v2 = Vector([1, 1, 0])
v3 = Vector([1, 1, 1])
basis = gram_schmidt([v1, v2, v3])
for i, u in enumerate(basis):
    print(f"u{i+1} = {u.vector}")
    print(f"  |u{i+1}| = {u.magnitude():.6f}")

print(f"u1 · u2 = {basis[0].dot(basis[1]):.6f}")
print(f"u1 · u3 = {basis[0].dot(basis[2]):.6f}")
print(f"u2 · u3 = {basis[1].dot(basis[2]):.6f}")