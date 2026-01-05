def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for name in names: 
        result[name] = names.count(name)

        return result
    

names =[ 'ali', 'vali', 'sami', 'gani', 'ali', 'ali', 'ali', 'vali', 'sami', 'sami', 'gani']
result = count_names(names=names)
print(result)