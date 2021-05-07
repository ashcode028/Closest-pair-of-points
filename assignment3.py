"""
CSE101: Introduction to Programming
Assignment 3

Name        :Ashita boyina
Roll-no     :2019028
"""



import math
import random



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    
    k=math.sqrt(abs((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)) 
    return k

def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    z=sorted(points,key=lambda x:x[0])
    return z    



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    z=sorted(points,key=lambda x:x[1])
    return z    



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
            



def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    l=len(points)
    d_final=d
    a=0
    b=0
    for i in range(l):
        for j in range(i+1,min(i+7,l)):
            d1=dist(points[i],points[j])
            if(d1<d_final) and d1!=0:
                a,b=points[i],points[j]
                d_final=d1
    if(d_final<d):
        return [d_final,a,b]
    else:
        return -1
               
    
    



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



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (10, 10) 
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    print(naive_closest_pair(plane))
    print(efficient_closest_pair(plane))
    