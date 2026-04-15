def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:
    if not points:
        return []

    if len(initial_centroids) != k:
        raise ValueError("initial_centroids length must equal k")

    dim = len(points[0])
    centroids = [tuple(float(x) for x in c) for c in initial_centroids]

    def square_distance(a, b):
        return sum((a[i] - b[i]) ** 2 for i in range(dim))

    def calculate_average(cluster):
        n = len(cluster)
        return tuple(sum(point[i] for point in cluster) / n for i in range(dim))

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            best_idx = 0
            best_distance = square_distance(centroids[0], point)

            for i in range(1, k):
                d = square_distance(centroids[i], point)
                if d < best_distance:
                    best_idx = i
                    best_distance = d

            clusters[best_idx].append(point)

        new_centroids = []
        for i in range(k):
            if clusters[i]:
                new_centroids.append(calculate_average(clusters[i]))
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return [tuple(round(x, 4) for x in centroid) for centroid in centroids]