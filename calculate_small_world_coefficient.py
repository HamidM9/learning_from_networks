def compute_small_world_coefficient(C, C_random, L, L_random):
    sigma = (C / C_random) / (L / L_random)
    return sigma


C_real = 0.4306
C_random = 0.0247
L_real = 6.0419
L_random = 3.7441


sigma = compute_small_world_coefficient(C_real, C_random, L_real, L_random)


print(f"Small-World Coefficient (σ): {sigma}")
