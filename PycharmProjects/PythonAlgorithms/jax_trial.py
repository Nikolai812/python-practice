import jax

# 1. Initialize the starting key (your line of code)
rng = jax.random.PRNGKey(0)

# 2. Split the key into a new key and a subkey
rng, subkey = jax.random.split(rng)

# 3. Use the subkey to actually generate a random number
random_matrix = jax.random.normal(subkey, (3, 3))

print(random_matrix)