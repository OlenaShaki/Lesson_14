class Tree:
    def __init__(self, values):
        self.value = None
        self.left = None
        self.right = None
        self.insert(values)

    def is_leaf(self):
        return self.left is None and self.right is None

    # додавання нового елементу
    def insert(self, values):
        if type(values) is list:
            for value in values:
                self.insert(value)
        else:
            if self.value is None:
                self.value = values
            elif values < self.value:
                if self.left is None:
                    self.left = Tree(values)
                else:
                    self.left.insert(values)
            elif values > self.value:
                if self.right is None:
                    self.right = Tree(values)
                else:
                    self.right.insert(values)

    # пошук мінімального значення
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.value

    # пошук максимального значення
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.value

    # видалення елементів
    def delete(self, values):
        if type(values) is list:
            for value in values:
                self.delete(value)
        else:
            if values == self.value:
                if self.is_leaf():
                    self.value = None
                elif self.left is None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                elif self.right is None:
                    self.value = self.left.value
                    self.left = self.left.left
                    self.right = self.left.right
                else:
                    self.value = self.right.min()
                    self.right.delete(self.value)
            elif values < self.value and self.left:
                if values == self.left.value and self.left.is_leaf():
                    self.left = None
                else:
                    self.left.delete(values)
            elif values > self.value and self.right:
                if values == self.right.value and self.right.is_leaf():
                    self.right = None
                else:
                    self.right.delete(values)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.is_leaf():
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


tree = Tree([9, 7, 4, 5, 6, 8, 16, 12, 11, 17, 180, 1])
tree.display()
tree.insert([2, 13])
tree.display()
tree.delete([10, 13, 17])
tree.display()
