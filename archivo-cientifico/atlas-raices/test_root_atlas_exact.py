import unittest
from root_atlas_exact import (root_atlas, reflection_closed, crystallographic,
                              antipodal_lines, length_shells, reflect, cartan_pair, failure_certificate, QPhi, vec, dot, preview_root_move,
                              reflection_closed_full_exact, crystallographic_full_exact)

def spaced_normals(roots, count):
    ordered=sorted(roots, key=lambda v: tuple((x.a,x.b) for x in v))
    return tuple(ordered[(len(ordered)*i)//count] for i in range(count))

class RootAtlasTests(unittest.TestCase):
    EXPECTED={'A2':6,'A3':12,'B3':18,'D4':24,'F4':48,'G2':12,'E6':72,'E7':126,'E8':240,'H3':30,'H4':120,
              'A4':20,'B4':32,'C3':18,'D5':40}

    def test_counts_antipodes_shells(self):
        for name,count in self.EXPECTED.items():
            with self.subTest(root=name):
                roots=root_atlas(name)
                self.assertEqual(len(roots),count)
                self.assertEqual(antipodal_lines(roots),count//2)
        self.assertEqual({str(k):v for k,v in length_shells(root_atlas('F4')).items()},
                         {'(2+0phi)':24,'(1+0phi)':24})
        self.assertEqual({str(k):v for k,v in length_shells(root_atlas('G2')).items()},
                         {'(6+0phi)':6,'(2+0phi)':6})

    def test_reflections_exact(self):
        for name in self.EXPECTED:
            with self.subTest(root=name):
                roots=root_atlas(name)
                normals=spaced_normals(roots,6) if len(roots)>30 else None
                self.assertTrue(reflection_closed(roots,normals=normals))

    def test_crystallographic_boundary(self):
        for name in ('A2','A3','A4','B3','B4','C3','D4','D5','F4','G2','E6','E7','E8'):
            with self.subTest(root=name):
                roots=root_atlas(name)
                normals=spaced_normals(roots,8) if len(roots)>30 else None
                self.assertTrue(crystallographic(roots,normals=normals))
        for name in ('H3','H4'):
            with self.subTest(root=name):
                roots=root_atlas(name)
                self.assertFalse(crystallographic(roots))
                self.assertIsNotNone(failure_certificate(roots))

    def test_reflection_involutive_and_metric(self):
        for name in self.EXPECTED:
            roots=root_atlas(name)
            sample=list(roots)[:4]
            for a in sample:
                for b in sample:
                    self.assertEqual(reflect(reflect(b,a),a), b)

    def test_counterexample_equal_cardinality_not_root_structure(self):
        fake=frozenset({vec((1,0)),vec((-1,0)),vec((0,1)),vec((0,-1)),
                        vec((1,2)),vec((-1,-2))})
        self.assertEqual(len(fake), len(root_atlas('A2')))
        self.assertFalse(reflection_closed(fake))

    def test_metric_and_cartan_gauge_equivariance(self):
        for name in self.EXPECTED:
            with self.subTest(root=name):
                sample=list(root_atlas(name))[:3]
                for a in sample:
                    for b in sample:
                        for c in sample:
                            rb=reflect(b,a)
                            rc=reflect(c,a)
                            self.assertEqual(dot(rb,rc), dot(b,c))
                            self.assertEqual(cartan_pair(rb,rc),cartan_pair(b,c))

    @staticmethod
    def all_supported():
        return ([f'A{n}' for n in range(1,9)]
                + [f'B{n}' for n in range(2,9)]
                + [f'C{n}' for n in range(2,9)]
                + [f'D{n}' for n in range(4,9)]
                + ['E6','E7','E8','F4','G2','H3','H4'])

    def test_classical_family_counts(self):
        for name in self.all_supported():
            family=name[0]
            if family not in 'ABCD':
                continue
            n=int(name[1:])
            expected={'A':n*(n+1),'B':2*n*n,'C':2*n*n,'D':2*n*(n-1)}[family]
            self.assertEqual(len(root_atlas(name)),expected)
            self.assertEqual(antipodal_lines(root_atlas(name)),expected//2)

    def test_all_roots_all_normals_exhaustive_exact(self):
        for name in self.all_supported():
            with self.subTest(root=name):
                roots=root_atlas(name)
                self.assertTrue(reflection_closed_full_exact(roots))
                self.assertEqual(crystallographic_full_exact(roots),name not in ('H3','H4'))

    def test_runtime_boundary_preview_does_not_authorize(self):
        roots=list(root_atlas('A2'))
        ev=preview_root_move('A2',roots[0],roots[1])
        self.assertTrue(ev.metric_preserved)
        self.assertTrue(ev.atlas_preserved)
        self.assertEqual(ev.action_eligibility,'NOT_EVALUATED')
        self.assertEqual(ev.authority,'NOT_EVALUATED')

    def test_a3_tetrahedron_root_mapping(self):
        self.assertEqual(len(root_atlas('A3')),4*3)
        self.assertEqual(antipodal_lines(root_atlas('A3')),6)

    def test_e8_full_root_shell(self):
        self.assertEqual(length_shells(root_atlas('E8')),{QPhi(2):240})

if __name__=='__main__': unittest.main()
