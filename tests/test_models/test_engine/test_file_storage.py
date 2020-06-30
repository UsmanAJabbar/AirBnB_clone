#!/usr/bin/python3
""" ksjadbf """
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ asmjsfb """
    def test_class_variables(self):
        """ slkjdfgh """
        subject = FileStorage()
        to_d = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for e in subject.all().keys():
            to_d.append(subject.all()[e])
        for e in to_d:
            del subject.all()[e.__class__.__name__ + '.' + e.id]

        # check attributes exist
        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))
        self.assertFalse(hasattr(subject, '__file_path'))
        self.assertFalse(hasattr(subject, '__objects'))
        del subject
        if os.path.exists('file.json'):
            print('file still exists')
            os.remove('file.json')

    def test_all(self):
        """ askjdfb """
        subject = FileStorage()
        to_d = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for e in subject.all().keys():
            to_d.append(subject.all()[e])
        for e in to_d:
            del subject.all()[e.__class__.__name__ + '.' + e.id]

        # check return
        self.assertIsInstance(subject.all(), dict)
        self.assertEqual(subject.all(), {})

        tmp1, tmp2 = BaseModel(), BaseModel()
        subject.new(tmp1)
        subject.new(tmp2)

        self.assertEqual(subject.all(), {'BaseModel.' + tmp1.id: tmp1,
                         'BaseModel.' + tmp2.id: tmp2})
        del tmp1
        del tmp2
        del subject

    def test_new(self):
        """ laskdfh """
        res = {"id": "8d8b1266-b706-4e9d-aeb9-70aae132d150",
               "__class__": "BaseModel",
               "updated_at": "2020-06-28T21:29:23.160292",
               "created_at": "2020-06-28T21:29:23.160254"}
        subject = FileStorage()
        to_d = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for e in subject.all().keys():
            to_d.append(subject.all()[e])
        for e in to_d:
            del subject.all()[e.__class__.__name__ + '.' + e.id]
        classes = [BaseModel(**res), User(**res), Place(**res), City(**res),
                   State(**res), Review(**res), Amenity(**res)]

        # check each class
        for cls in classes:
            subject.new(cls)
            self.assertIn(cls.__class__.__name__ + '.' + cls.id,
                          subject.all())

        # check each key
        for cls in classes:
            name = cls.__class__.__name__
            self.assertTrue(name + '.' + cls.id in subject.all().keys())

        # check each object
        for i in range(len(subject.all().keys())):
            self.assertIn(subject.all()[list(subject.all().keys())[i]],
                          classes)
        for e in classes:
            del e
        del subject

    def test_save(self):
        """ skljdfh """
        res = '{"BaseModel.8d8b1266-b706-4e9d-aeb9-70aae132d150": {"id\
": "8d8b1266-b706-4e9d-aeb9-70aae132d150", "__class__\
": "BaseModel", "updated_at": "2020-06-28T21:29:23.160292", "created_at\
": "2020-06-28T21:29:23.160254"}}'
        subject = FileStorage()
        to_d = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for e in subject.all().keys():
            to_d.append(subject.all()[e])
        for e in to_d:
            del subject.all()[e.__class__.__name__ + '.' + e.id]
        tmp = BaseModel(**json.loads(res)["\
BaseModel.8d8b1266-b706-4e9d-aeb9-70aae132d150"])
        subject.new(tmp)

        # test no file
        if os.path.exists('file.json'):
            os.remove('file.json')
        subject.save()
        self.assertTrue(os.path.exists('file.json'))
        if os.path.exists('file.json'):
            with open('file.json') as f:
                self.assertEqual(res[:52], f.read()[:52])

        # test with file
        with open('file.json', 'w') as f:
            f.write("eggyboiiii")
        subject.save()
        with open('file.json') as f:
            self.assertEqual(res[:52], f.read()[:52])
        del tmp
        del subject

    def test_reload(self):
        """ skjdfh """
        res = '{"BaseModel.8d8b1266-b706-4e9d-aeb9-70aae132d150": {"id\
": "8d8b1266-b706-4e9d-aeb9-70aae132d150", "__class__\
": "BaseModel", "updated_at": "2020-06-28T21:29:23.160292", "created_at\
": "2020-06-28T21:29:23.160254"}}'
        subject = FileStorage()
        to_d = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for e in subject.all().keys():
            to_d.append(subject.all()[e])
        for e in to_d:
            del subject.all()[e.__class__.__name__ + '.' + e.id]

        # test no file
        if os.path.exists('file.json'):
            os.remove('file.json')
        subject.reload()
        self.assertEqual(subject.all(), {})

        # test empty file
        with open('file.json', 'w') as f:
            f.write("")
        with self.assertRaises(Exception):
            subject.reload()
        self.assertEqual(subject.all(), {})

        # test nonempty file
        tmp = BaseModel(**json.loads(res)['\
BaseModel.8d8b1266-b706-4e9d-aeb9-70aae132d150'])
        subject.new(tmp)
        subject.save()
        del subject.all()['BaseModel.8d8b1266-b706-4e9d-aeb9-70aae132d150']
        subject.reload()
        self.assertEqual(subject.all().keys(), {'\
BaseModel.8d8b1266-b706-4e9d-aeb9-70aae132d150': tmp}.keys())
        del tmp
        del subject
