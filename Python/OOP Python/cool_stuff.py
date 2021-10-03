# This is the ILikeCats class
class ILikeCats:
    ''' The pass keyword is a placeholder that
        indicates that no further action needs to
        be taken
    '''
    pass

# This is the ILikeDogs class
class ILikeDogs:
    # The TypeOfDog method
    def TypeOfDog(self):
        self.breed = ""
        self.personality = ""
        self.color = ""
    

# This is the ILikeShoes class
class ILikeShoes:
    def ShoeType(self):
        self.color_of_shoe = ""
        self.size_of_shoe = 0
        self.brand_of_shoe = ""


# This is the ILikeLife class
class ILikeLife:
    pass

shoes = ILikeShoes()
shoes.ShoeType()
shoes.color_of_shoe = "red"
shoes.size_of_shoe = 11
shoes.brand_of_shoe = "Nike"

print(shoes.color_of_shoe, shoes.size_of_shoe, shoes.brand_of_shoe)