flatten = lambda list_: eval('[' + str(list_).replace('[', '').replace(']', '') + ']')

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = flatten(list_of_list)

    def __iter__(self):
        self.index_ = -1
        return self

    def __next__(self):
        self.index_ += 1
        if self.index_ == len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.index_]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()