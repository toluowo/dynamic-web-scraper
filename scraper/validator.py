from pydantic import BaseModel, validator

class Book(BaseModel):
    title: str
    price: float
    availability: str

    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

    @validator("title")
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be empty")
        return v


def validate_data(df):
    validated = []

    for _, row in df.iterrows():
        try:
            book = Book(**row.to_dict())
            validated.append(book.dict())
        except Exception as e:
            print(f"Validation error: {e}")

    return validated
