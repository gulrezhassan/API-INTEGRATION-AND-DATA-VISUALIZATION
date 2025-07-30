from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score , classification_report

#in this example we will create a small dataset of email text and labels (0 for not spam, 1 for spam)

email_data =[
    "get rich quick ! click here to win a lottery!",
    "hello friend, how are you doing today?",
    "urgent: your account has been compromised, please reset your password",
    "limited time offer: buy one get one free on all products",
    "meeting reminder for tomorrow at 10 AM",
    "congratulations! you have won a free vacation",
]

labels = [0, 0, 0, 0,1,1]  # Corresponding labels for the emails

# Convert text data to numerical data using CountVectorizer
vectorizer = CountVectorizer()
x=vectorizer.fit_transform(email_data)

#split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size=0.2,random_state=42)

#create a multinomial Naive Bayes classifier
classifier = MultinomialNB()

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy",accuracy)
print("Classification Report:\n", report)

#predict whether a new email is spam or not
new_email = ["Congratulations! You've been selected for a free gift card!"]
new_email_vectorized = vectorizer.transform(new_email)
prediction = classifier.predict(new_email_vectorized)

if prediction[0] == 0:
    print("The email is not spam.")
else:
    print("The email is spam.")

