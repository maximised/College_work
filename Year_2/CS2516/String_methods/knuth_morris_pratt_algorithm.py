def knuth_morris_pratt(target, source):
    """
    Returns the position of the first found match of target inside source text

    Worst case time compexity: O(n+m), n is len(source), m is len(target)

    :param target: The text we try to find in source
    :param source: The source text
    :return: position of the target in source or -1 if not found
    """
    j = 0  # the current index in source being checked
    i = 0  # the current index in target being checked
    pi = [0]*len(target)
    compute_pi(target, pi)

    while i < len(target) and j < len(source):
        if target[i] == source[j]:  # current chars match
            i += 1
            j += 1
        elif i == 0:  # failed match with start of target
            j += 1    # so force a step forward
        else:
            i = pi[i-1]  # jump forward (note: j does not move)

    if i == len(target):
        return j - len(target)
    else:
        return -1


def compute_pi(target, pi):
    """
    Creates the pi table

    Worst time complexity: O(m), m is len(target)

    :param target: text to find in source
    :param pi: table for the target string
    """
    pi[0] = 0
    for i in range(1, len(target)):
        if target[ i ] == target[ pi[i-1] ]:
            pi[i] = pi[i-1] + 1
        else:
            pi[i] = 0



#################################################################
# Test code

source = "A digger is an amalgamtor and can amalgamate the streets."
target = "amalgamate"

pos = knuth_morris_pratt(target, source)
print(pos)
print(source[pos:])


