import math




def main():
    radius_list= [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    name_list = ['#1 Picnic','#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5','#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    #print("This program can compute the storage efficeiency of a tin can. You must enter the height and radius of the can for it to work.")
    print("The top 12 cans and their surface area")


    # [print (i) for i in name_list]
    for i in range(len(radius_list)):
        radius= radius_list[i]
        height = height_list[i]
        name = name_list[i]
        # call functions
        #computing the volume
        def compute_volume(radius, height):
            volume= math.pi*radius **2*height
            return volume

        #computing the surface area
        def compute_surface_area(radius, height):
            surface_area= 2*math.pi * radius*(radius + height)
            return surface_area

        def compute_efficiency(volume, surface_area):
            storage_efficiency= volume / surface_area
            return storage_efficiency

        volume = compute_volume(radius, height)
        surface_area= compute_surface_area(radius, height)
        storage_efficiency = compute_efficiency(volume, surface_area)
        
        print(f"{name:13} {storage_efficiency:.1f}")
        # :13 like in name above, helps put space between that variable and the next input/variable



#name    radius   hieght
#1 Picnic	6.83	10.16
#1 Tall	7.78	11.91
#2	8.73	11.59
#2.5	10.32	11.91
#3 Cylinder	10.79	17.78
#5	13.02	14.29
#6Z	5.40	8.89
#8Z short	6.83	7.62
#10	15.72	17.78
#211	6.83	12.38
#300	7.62	11.27
#303	8.10	11.11	

main()