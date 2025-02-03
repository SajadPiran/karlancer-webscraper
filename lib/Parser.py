from bs4 import BeautifulSoup, ResultSet

class Parser :

    def __init__( self, content : str ):

        self.content = content
        self.__soup = BeautifulSoup( self.content , 'html.parser' )

    def __get_all_projects( self ) -> ResultSet :
        return self.__soup.find_all('app-sidebar-project-card')

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

        for i in range( len( link ) ) :

            data.append( {
                'title' : title[i].text,
                'link' : f'https://www.karlancer.com{ link[i]['href'] } ' ,
                'release_time' : release_time[i].text
            } )

        return data