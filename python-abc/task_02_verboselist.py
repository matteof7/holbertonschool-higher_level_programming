class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        else:
            print(f"[{item}] not found in the list.")

    def pop(self, index=-1):
        if self:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        else:
            print("Cannot pop from an empty list.")
            raise IndexError("pop from empty list")
