import redis
import time
import json

# Connect to the local Redis server (assuming it's running on the default port 6379)
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def expensive_function(x):
    # Simulate an expensive computation
    time.sleep(2)
    return x * x

def cached_expensive_function(x):
    # Check if the result is already in the cache
    cache_key = f"expensive_function:{x}"
    cached_result = redis_client.get(cache_key)

    if cached_result is not None:
        # If the result is in the cache, return it
        print("Result retrieved from cache.")
        return json.loads(cached_result)
    else:
        # If the result is not in the cache, calculate it and store it in the cache
        result = expensive_function(x)
        redis_client.set(cache_key, json.dumps(result))
        return result

# Test the cached_expensive_function
start_time = time.time()
result1 = cached_expensive_function(5)
print(f"First call result: {result1}, Time taken: {time.time() - start_time:.2f} seconds")

# Call the function again with the same argument
start_time = time.time()
result2 = cached_expensive_function(5)
print(f"Second call result: {result2}, Time taken: {time.time() - start_time:.2f} seconds")

# Call the function with a different argument
start_time = time.time()
result3 = cached_expensive_function(10)
print(f"Third call result: {result3}, Time taken: {time.time() - start_time:.2f} seconds")
