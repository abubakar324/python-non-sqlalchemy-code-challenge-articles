class Article:
    all = []
    def __init__(self, author, magazine, title):
        
        if not isinstance (title, str):
            raise TypeError("Title must be a string")
        if not (5 <=  len(title)<=50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        pass


  
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('Name should be a string')
        if len(name) == 0:
               raise ValueError('Name must be longer than 0 characters')
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        categories = list(set([article.magazine.category for article in self.articles()]))
        return categories if categories else None


    @name.setter
    def name(self,value):
        pass

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name,str):
            raise TypeError('Names must be string')
        if not(2<= len(name) <=16):
            raise ValueError('Names must be between 2 and 16 characters')
        if not isinstance(category,str):
            raise TypeError('category must be a string')
        if len(category)==0:
            raise ValueError('category must be longer than 0 character')

        self._name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors()
               if len([article for article in Article.all if article.author == author and article.magazine == self]) > 2]
        return authors if authors else None