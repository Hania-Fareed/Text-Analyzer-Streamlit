import streamlit as st
import re

def analyze_text(text):
    words = text.split()
    total_words = len(words)
    total_characters = len(text)
    
    # Count vowels
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Check for 'Python' in text
    contains_python = "Python" in text
    
    # Calculate average word length
    avg_word_length = total_characters / total_words if total_words > 0 else 0
    
    return total_words, total_characters, vowel_count, contains_python, avg_word_length

def main():
    st.title("Text Analyzer")
    
    # User input
    paragraph = st.text_area("Enter a paragraph:")
    
    if paragraph.strip():
        total_words, total_characters, vowel_count, contains_python, avg_word_length = analyze_text(paragraph)
        
        # Display analysis results
        st.subheader("Analysis Results")
        st.write(f"✅ **Total Words:** {str(total_words)}")
        st.write(f"✅ **Total Characters (including spaces):** {str(total_characters)}")
        st.write(f"✅ **Vowel Count:** {str(vowel_count)}")
        st.write(f"✅ **Contains 'Python'?:** {'Yes' if contains_python else 'No'}")
        st.write(f"✅ **Average Word Length:** {avg_word_length:.2f}")
        
        # Search and Replace
        st.subheader("Search and Replace")
        search_word = st.text_input("Enter word to search:")
        replace_word = st.text_input("Enter word to replace with:")
        
        if search_word and replace_word:
            modified_text = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, paragraph)
            st.text_area("Modified Paragraph:", modified_text, height=150)
        
        # Case conversions
        st.subheader("Case Conversions")
        st.text_area("Uppercase:", paragraph.upper(), height=150)
        st.text_area("Lowercase:", paragraph.lower(), height=150)
    else:
        st.warning("⚠️ Please enter a paragraph to analyze.")

if __name__ == "__main__":
    main()
