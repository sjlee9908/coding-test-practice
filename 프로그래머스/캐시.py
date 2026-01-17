def solution(cacheSize, cities):
    answer = 0
    cache = [0] * cacheSize

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            idx = cache.index(city)
            cache = [cache[idx]] + cache[0:idx] + cache[idx+1:]
        else:
            cache.insert(0, city)
            answer += 5
        if len(cache) > cacheSize:
            del cache[-1]

    return answer

print(
    solution(
3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    )
)