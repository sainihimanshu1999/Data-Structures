'''In this we do dfs traversal of both the trees and at the same time and then return the reference node'''


def targetCopy(target,original,cloned):
    if not original: return None
    if original ==  target: return cloned
    return targetCopy(original.left,cloned.left,target) or targetCopy(original.ight,cloned.right,target)
