from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from guy.models import Guy

class GuyMethodTests(TestCase):

    def test_create_method(self):
        """
        Make sure the create method creates a guy at the location expected.
        Also ensure the name is present
        """
        g = Guy.create('foobar')
        self.assertEqual(g.position.x, 0)
        self.assertEqual(g.position.y, 0)
        self.assertEqual(g.position.dir, 0)
        self.assertEqual(g.name, 'foobar')
        self.assertRaises(TypeError, Guy.create)

        g = Guy.create('Eric', 1, 3, 2)
        self.assertEqual(g.position.x, 1)
        self.assertEqual(g.position.y, 3)
        self.assertEqual(g.position.dir, 2)
        self.assertEqual(g.name, 'Eric')

        g = Guy.create('Eric', 1, 3)
        self.assertEqual(g.position.x, 1)
        self.assertEqual(g.position.y, 3)
        self.assertEqual(g.position.dir, 0)
        self.assertEqual(g.name, 'Eric')

        g = Guy.create('Eric', 1)
        self.assertEqual(g.position.x, 1)
        self.assertEqual(g.position.y, 0)
        self.assertEqual(g.position.dir, 0)
        self.assertEqual(g.name, 'Eric')

    def test_start_pos_is_origin(self):
        """
        When a empty guy is saved, his position is 0, 0 and he should be facing North
        """
        g = Guy()
        g.save()
        self.assertEqual(g.position.x, 0)
        self.assertEqual(g.position.y, 0)
        self.assertEqual(g.position.dir, 0)

    def test_turn(self):
        """
        Turn right should yield a dir number one greater than currently, unless he's facing west (3)
        Turn left should yield a dir number one less than currently, unless he's facing north (0)
        Should raise a key error if the input isn't 'r', 'l', 'f', 'b', or 's'
        """
        g = Guy()
        g.save()
        g.turn('r')
        self.assertEqual(g.position.dir, 1)
        g.turn('l')
        self.assertEqual(g.position.dir, 0)
        g.turn('l')
        self.assertEqual(g.position.dir, 3)
        g.turn('l')
        self.assertEqual(g.position.dir, 2)
        g.turn('l')
        self.assertEqual(g.position.dir, 1)
        g.turn('r')
        self.assertEqual(g.position.dir, 2)

        self.assertRaises(KeyError, g.turn, 'asdfasdf')

    def test_move(self):
        """
        Test that moving a guy yields the appropriate position
        """
        g = Guy()
        g.save()
        g.move('f')
        self.assertEqual(g.position.x, 0)
        self.assertEqual(g.position.y, 1)
        self.assertEqual(g.position.dir, 0)
        g.move('b')
        self.assertEqual(g.position.x, 0)
        self.assertEqual(g.position.y, 0)
        self.assertEqual(g.position.dir, 0)
        g.turn('r')
        g.move('f')
        self.assertEqual(g.position.x, 1)
        self.assertEqual(g.position.y, 0)
        self.assertEqual(g.position.dir, 1)
        g.move('b')
        g.move('b')
        self.assertEqual(g.position.x, -1)
        self.assertEqual(g.position.y, 0)
        self.assertEqual(g.position.dir, 1)
        g.turn('r')
        g.move('f')
        g.move('f')
        self.assertEqual(g.position.x, -1)
        self.assertEqual(g.position.y, -2)
        self.assertEqual(g.position.dir, 2)
        g.move('b')
        g.move('b')
        g.move('b')
        self.assertEqual(g.position.x, -1)
        self.assertEqual(g.position.y, 1)
        self.assertEqual(g.position.dir, 2)
        g.turn('r')
        g.move('f')
        g.move('f')
        g.move('f')
        self.assertEqual(g.position.x, -4)
        self.assertEqual(g.position.y, 1)
        self.assertEqual(g.position.dir, 3)

class GuyViewTests(TestCase):
    
    def test_index_with_no_guys(self):
        """
        If index yields no guys, make sure the table has "No Guys" message.
        """
        response = self.client.get(reverse('guy:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Guys")
        self.assertQuerysetEqual(response.context['guys'], [])

    def test_index_with_1_guy(self):
        """
        Create a guy, make sure he shows up if the owner matches the logged-in user
        """
        u = User(username="tester")
        u.set_password("123456")
        u.save()
        self.client.login(username=u.username, password="123456")
        g = Guy(name="Test Guy", owner=u)
        g.save()
        response = self.client.get(reverse('guy:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Guy")
        self.assertQuerysetEqual(response.context['guys'], ['<Guy: Test Guy, X: 0, Y: 0, DIR: North>',])
