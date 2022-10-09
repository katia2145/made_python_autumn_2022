class LRUCache:
    def __init__(self, limit=42):
        self.cache_size = limit
        self.values = {}
        self.priority = {}
        self.cur_time = 1

    def get(self, key):
        if key not in self.values.keys():
            return None
        
        self.set_priprity(key)
        return self.values[key]
    
    def set(self, key, value):
        if key in self.priority.keys():
            self.set_priprity(key)
            self.values[key] = value

        else:
            if len(self.values) >= self.cache_size:
                key_with_min_priority = self.find_key_with_min_priority()
                self.priority.pop(key_with_min_priority, None)
                self.values.pop(key_with_min_priority, None)

            self.values[key] = value
            self.set_priprity(key)
    
    def set_priprity(self, key):
        self.priority[key] = self.cur_time
        self.cur_time += 1
    
    def find_key_with_min_priority(self):
        key_with_min_priority = None
        min_priority = 1e9

        for key in self.priority.keys():
            if self.priority[key] < min_priority:
                min_priority = self.priority[key]
                key_with_min_priority = key
        
        return key_with_min_priority
