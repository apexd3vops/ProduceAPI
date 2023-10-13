from sqlalchemy import Column, Integer, String, TIMESTAMP, text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Admins(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    strUsername = Column(String, nullable=False, unique=True)
    strPassword = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()') )
    
class Categories(Base): 
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    strCategory = Column(String, nullable=False, unique=True)
    strCatDescription = Column(String, nullable= False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Produce(Base):
    __tablename__ = 'produce'
    id = Column(Integer, primary_key=True, nullable=False)
    strProduce = Column(String, nullable=False)
    strDescription = Column(String, nullable=False)
    strContact = Column(String, nullable= False)
    strProduceThumb = Column(String, nullable=False)
    # strTags = TODO: How do you add a list to a database
    on_sale = Column(Boolean, nullable=False, server_default='False')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    strCategory = Column(String, ForeignKey("categories.strCategory", ondelete="CASCADE"), nullable=True)

  # ForeignKey modified
    strCatDescription = Column(String, ForeignKey("categories.strCatDescription", ondelete="CASCADE"), nullable=True)
    # created_by = TODO: Add a column to show admin active on the server. It should track who adds a produce and who verifies purchase. Vendors earn money from approving transactions. Is blockchain technology possible and how should I implement it here.



    

    
