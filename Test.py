# coding=utf-8
__author__ = 'g7842'

from JsonParser import JsonParser
import unittest

TEST_SAMPLE = '''
{"key":[
    {},
    [],
    100,
    true,
    false,
    null,
    {
        "obj":  {},
        "list": [],
        "inter":100,
        "bool": true
    }
    ]
}'''


class JsonParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = JsonParser()
        self.maxDiff = None

    def test_main(self):
        file_path = "testReport.json"
        a1 = JsonParser()
        a2 = JsonParser()
        a3 = JsonParser()

        # test_json_str、test_dict
        a1.load(TEST_SAMPLE)
        d1 = a1.dump_dict()
        # 粗糙比较test_dict和d1

        a2.load_dict(d1)
        a2.dump_json(file_path)
        a3.load_json(file_path)
        d3 = a3.dump_dict()
        # 比较d1和d3是否完全一样
        self.assertEqual(d1, d3)
        print('test main finish')


if __name__ == '__main__':
    unittest.main()