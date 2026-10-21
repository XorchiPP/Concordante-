"""Generate finite exact checks using the atlas and the Python standard library."""
import json
from root_atlas_exact import root_atlas, antipodal_lines, length_shells, reflection_closed_full_exact, crystallographic_full_exact

def main():
    names=([f'A{n}' for n in range(1,9)]+[f'B{n}' for n in range(2,9)]+[f'C{n}' for n in range(2,9)]+[f'D{n}' for n in range(4,9)]+['E6','E7','E8','F4','G2','H3','H4'])
    atlas={}
    for name in names:
        roots=root_atlas(name)
        atlas[name]={'roots':len(roots),'unoriented_root_lines':antipodal_lines(roots),'norm_sq_shells':{str(k):v for k,v in length_shells(roots).items()},'reflection_all_roots_all_normals':'PASS' if reflection_closed_full_exact(roots) else 'FAIL','crystallographic':crystallographic_full_exact(roots)}
    print(json.dumps({'description':'Finite coordinate checks, not a classification proof or physical validation','tested_system_count':len(atlas),'root_normal_pair_count':sum(v['roots']**2 for v in atlas.values()),'atlas':atlas},indent=2,sort_keys=True))
if __name__=='__main__':
    main()
