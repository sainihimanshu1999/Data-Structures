import pyhash
bit_vector = [0] * 20
print(bit_vector)

#non cryptographic hash fucntions (Murmur and  FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

#calculating the output of FNV and MURMUR hash functions for Pokemons   
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmender") % 20
murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

print(fnv_pika)
print(fnv_char)
print(murmur_pika)
print(murmur_char)
