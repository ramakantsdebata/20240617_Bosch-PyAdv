from concurrent.futures import ProcessPoolExecutor
import hashlib

texts = [b"the quick brown fox jmped over the lazy dog",
         b"the big fat panda sat on the hungry snake", 
         b"the slick mountain lion ran uo the tall tree"]

def generate_hash(text):
    return hashlib.sha3_384(text).hexdigest()

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        for text, hash_t in zip(texts, executor.map(generate_hash, texts)):
            print(f"{text} hash is: {hash_t}")
