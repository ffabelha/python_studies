#!/usr/bin/env python3

import unittest


class Candy():
    """Candy abstract class"""

    def name(self):
        return 'Candy'

    def show_recipes(self): pass


class Cookie(Candy):
    """Cookie class"""

    def name(self):
        return 'Cookie'

    def show_recipes(self):
        return ['all-purpose flour', 'margarine', 'sugar', 'eggs', 'milk']


class Lollipop(Candy):
    """Lollipop class"""

    def name(self):
        return 'Lollipop'

    def show_recipes(self):
        return ['sugar', 'artificial flavour']


class CandyFactory():
    """CandyFactory abstract class"""

    def make(self): return None


class CookieFactory(CandyFactory):
    """CookieFactory concrete class"""

    def make(self):
        return Cookie()


class LollipopFactory(CandyFactory):
    """LollipopFactory concrete class"""

    def make(self):
        return Lollipop()


# Model tests

class CandyTests(unittest.TestCase):

    def setUp(self):
        self.candy = Candy()

    # test if Candy exists
    def test_if_candy_exists(self):
        self.assertIsNotNone(self.candy, 'Candy not exists.')

    # test Candy should knows it's name
    def test_candy_should_knows_its_name(self):
        self.assertEqual(self.candy.name(),
                         'Candy',
                         "Candy doesn't know it's name")

    # test Candy should not knows it's recipes because it's too generic
    def test_candy_should_not_knows_its_recipes_because_its_too_generic(self):
        self.assertIsNone(self.candy.show_recipes(),
                          "Candy knows it's recipes")

    def tearDown(self):
        pass


class CookieTests(unittest.TestCase):

    def setUp(self):
        self.cookie = Cookie()

    # test if cookie exists
    def test_if_cookie_exists(self):
        self.assertIsNotNone(self.cookie, 'Cookie not exists.')

    # test cookie should knows it's name
    def test_cookie_should_knows_its_name(self):
        self.assertEqual(self.cookie.name(),
                         'Cookie',
                         "Cookie doesn't know it's name")

    # test cookie has recipes
    def test_cookie_has_recipes(self):
        self.assertGreater(len(self.cookie.show_recipes()),
                           0,
                           "Cookie knows it's recipes")

    def tearDown(self):
        pass


class LollipopTests(unittest.TestCase):

    def setUp(self):
        self.lollipop = Lollipop()

    # test if lollipop exists
    def test_if_lollipop_exists(self):
        self.assertIsNotNone(self.lollipop, 'Lollipop not exists.')

    # test lollipop should knows it's name
    def test_lollipop_should_knows_its_name(self):
        self.assertEqual(self.lollipop.name(),
                         'Lollipop',
                         "Lollipop doesn't know it's name")

    # test lollipop has recipes
    def test_lollipop_has_recipes(self):
        self.assertGreater(len(self.lollipop.show_recipes()),
                           0,
                           "Lollipop knows it's recipes")

    def tearDown(self):
        pass


# Factory tests


class CandyFactoryTests(unittest.TestCase):

    def setUp(self):
        self.candy_factory = CandyFactory()

    # candy factory exists?
    def test_if_candy_factory_exists(self):
        self.assertIsNotNone(self.candy_factory, 'CandyFactory not exists.')

    # candy factory should not create anything
    def test_candy_factory_should_not_create_anything(self):
        self.assertIsNone(self.candy_factory.make(),
                          'CandyFactory created something.')

    def tearDown(self):
        pass


class CookieFactoryTests(unittest.TestCase):

    def setUp(self):
        self.cookie_factory = CookieFactory()

    # cookie factory exists?
    def test_if_cookie_factory_exists(self):
        self.assertIsNotNone(self.cookie_factory, 'CookieFactory not exists.')

    # cookie factory should create a cookie
    def test_cookie_factory_should_create_a_cookie(self):
        a_cookie = self.cookie_factory.make()
        self.assertTrue(a_cookie and isinstance(a_cookie, Cookie),
                        "CookieFactory didn't create a cookie.")

    # cookie factory should create only cookies
    def test_cookie_factory_should_create_only_cookies(self):
        made_cookies = [self.cookie_factory.make() for i in range(10)]
        made_anything_else = [not_a_cookie for cookie in made_cookies
                              if not isinstance(cookie, Cookie)]

        self.assertEqual(len(made_anything_else),
                         0,
                         'CookieFactory create something else than cookies.')

    def tearDown(self):
        pass


class LollipopFactoryTests(unittest.TestCase):

    def setUp(self):
        self.lollipop_factory = LollipopFactory()

    # lollipop factory exists?
    def test_if_lollipop_factory_exists(self):
        self.assertIsNotNone(self.lollipop_factory,
                             'LollipopFactory not exists.')

    # lollipop factory should create a cookie
    def test_lollipop_factory_should_create_a_cookie(self):
        a_lollipop = self.lollipop_factory.make()
        self.assertTrue(a_lollipop and isinstance(a_lollipop, Lollipop),
                        "LollipopFactory didn't create a lollipop.")

    # lollipop factory should create only lollipop
    def test_lollipop_factory_should_create_only_lollipopies(self):
        made_lollipopies = [self.lollipop_factory.make() for i in range(10)]
        made_anything_else = [not_a_lollipop for lollipop in made_lollipopies
                              if not isinstance(lollipop, Lollipop)]

        self.assertEqual(len(made_anything_else),
                         0,
                         'LollipopFactory create something'
                         'else than lollipopies.')

    def tearDown(self):
        pass
