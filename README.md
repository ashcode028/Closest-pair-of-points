# Closest-pair-of-points
    1.DIVIDE-CONQUER ALGORITHM
	2.Finding closest pair of coordinates in 2D
	3.NAIVE AND EFFICIENT APPROACH EMPLEMENTED
### Naive Implementation
```
def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    d=dist(plane[0],plane[1])
    p1=plane[0]
    p2=plane[1]
    for i in range(len(plane)):
        for j in range(i+1,len(plane)):
            d1=dist(plane[i],plane[j])
            if(d>d1 and d1!=0):
                d=d1
                p1=plane[i]
                p2=plane[j]
    return [d,p1,p2]
            
```
### Efficient Closest Pair
Recurisve algorithm which finds using strip method.
```
def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    p_x=sort_points_by_X(points)
    result=efficient_closest_pair_routine(p_x)
    return result

```
```
def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    l=len(points)
    if (l<=3):
        return naive_closest_pair(points)
        
    else:
        mid=l//2
        mid_x=points[l//2][0]
        l_x=points[:mid]
        r_x=points[mid:]
        result=[None,None,None]
        
        d1=efficient_closest_pair_routine(l_x)
        d2=efficient_closest_pair_routine(r_x)
        
        if(d1[0]>d2[0]):
            result=d2
        else:
            result=d1
        region=[]
        for i in points:
            if (mid_x-result[0]<=i[0]<=mid_x+result[0]):
                region.append(i)
        test=closest_pair_in_strip(region,result[0])
        if (test!=-1):
            result=test
        return result   
                                                               
```
