from bs4 import BeautifulSoup, ResultSet

class Parser :

    def __init__( self, content : str ):

        self.content = content
        self.__soup = BeautifulSoup( self.content , 'html.parser' )

    def __get_all_projects( self ) -> ResultSet :
        class_name = 'bg-white br-9 text-right position-relative border-1-transparent card-hover p-30-20'
        return self.__soup.find_all( 'div' , attrs= { 'class' : class_name } )

    def get_data_from_project( self , content : str , attr : {} = {}  ) -> list[ ResultSet ] :

        data_list = []
        projects = self.__get_all_projects()

        for data in projects :

            data_list.append( data.find( content , attr ) )

        return data_list

    def get_all_data( self ) -> list[ dict[ str,str ] ] :

        data = []
        link = self.get_data_from_project( 'a' )
        title = self.get_data_from_project( 'h4' )
        release_time = self.get_data_from_project( 'span' , { 'class' : 'color-white' } )
        price = self.get_data_from_project('div' , { 'class' : 'fs-16 b-900 mr-2 ml-1' } )

        for i in range( len( link ) ) :

            data.append( {
                'title' : title[i].text,
                'link' : f'https://www.karlancer.com{ link[i]['href'] } ' ,
                'release_time' : release_time[i].text,
                'price' : price[i].text
            } )

        return data