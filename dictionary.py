# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький
# або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти
# переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник
# звернень);
# ■ відображати топ-10 найнепопулярніших слів
# (визначаємо непопулярність спираючись на лічильник
# звернень).
# Використовуйте дерево для виконання цього
# завдання.


class TreeNode:
    def __init__(self, key, translation):
        self.key = key
        self.translation = translation
        self.left = None
        self.right = None
        self.counter = 0

class DictionaryTree:
    def __init__(self):
        self.root = None
        self.popular = []
        self.unpopular = []

    def add_word(self, key, translation):
        if not self.root:
            self.root = TreeNode(key, translation)
        else:
            self._add_word(self.root, key, translation)

    def _add_word(self, node, key, translation):
        if key == node.key:
            node.translation = translation
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, translation)
            else:
                self._add_word(node.left, key, translation)
        else:
            if node.right is None:
                node.right = TreeNode(key, translation)
            else:
                self._add_word(node.right, key, translation)

    def remove_word(self, key):
        self.root = self._remove_word(self.root, key)

    def _remove_word(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._remove_word(node.left, key)
        elif key > node.key:
            node.right = self._remove_word(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            successor = self._find_min(node.right)
            node.key, node.translation = successor.key, successor.translation
            node.right = self._remove_word(node.right, successor.key)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
        
        

    def show_translation(self, key):
        node = self._search(self.root, key)
        if node:
            node.counter += 1
            return f"{node.key} - {node.translation}"
        else: return None
    
    def _search(self, node, key):
        if not node or node.key == key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def display_top_popular(self):

        self._get_popular_words(self.root)
        if self.popular:
            print("Топ 10")
            for word in self.popular[:10]:
                print(f'{word.key}: {word.counter} було переглянуто разів')


    def _get_popular_words(self, node):
        if node is not None:
            self._get_popular_words(node.left)
            self.popular.append(node)
            self.popular.sort(key=lambda x: x.counter, reverse=True)
            if len(self.popular)>10:
                self.popular.pop()
            self._get_popular_words(node.right)

    def display_low_popular(self):

        self._get_unpopular_words(self.root)
        if self.unpopular:
            print("Low 10")
            for word in self.unpopular[:10]:
                print(f'{word.key}: {word.counter} було переглянуто разів')


    def _get_unpopular_words(self, node):
        if node is not None:
            self._get_unpopular_words(node.left)
            self.unpopular.append(node)
            self.unpopular.sort(key=lambda x: x.counter)
            if len(self.unpopular)>10:
                self.unpopular.pop()
            self._get_unpopular_words(node.right)

dictionary = DictionaryTree()
dictionary.add_word("der Apfel", "яблуко")
dictionary.add_word("die Banane", "банан")
dictionary.add_word("das Auto", "автомобиль")
dictionary.add_word("die Lampe", "лампа")
dictionary.add_word("das Bier", "пиво")
dictionary.add_word("der Zug", "поезд")
dictionary.add_word("der Bus", "автобус")
dictionary.add_word("die Bibel", "библия")
dictionary.add_word("das Flugzeug", "самолет")
dictionary.add_word("der Führerschein", "водительское удостоверение")
dictionary.add_word("der Krankenwagen", "скорая помощь")
dictionary.add_word("das Krankenhaus", "больница")
dictionary.add_word("der Kugelschreiber", "ручка")
dictionary.add_word("der Weihnachtsbaum", "рождественская елка")

print(dictionary.show_translation("der Apfel"))
print(dictionary.show_translation("der Zug"))
print(dictionary.show_translation("die Bibel"))
print(dictionary.show_translation("die Bibel"))
print(dictionary.show_translation("die Bibel"))
print(dictionary.show_translation("der Weihnachtsbaum"))
print(dictionary.show_translation("der Weihnachtsbaum"))
print(dictionary.show_translation("der Kugelschreiber"))
print(dictionary.show_translation("das Bier"))
print(dictionary.show_translation("die Lampe"))
print(dictionary.show_translation("das Auto"))
print(dictionary.show_translation("der Führerschein"))
print(dictionary.show_translation("die Banane"))

print()
dictionary.remove_word("der Bus")
print()
print(dictionary.show_translation("der Bus"))

print()
dictionary.display_top_popular()
print()
dictionary.display_low_popular()