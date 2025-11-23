from Sentiment_Module.emotion_detector import emotion_detector
import unittest 

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector(self):
        result1 = emotion_detector("I feel alive and full of joy")
        self.assertEqual(result1, 'joy')
        
        result2 = emotion_detector("I feel really mad about this")
        self.assertEqual(result2, 'anger')

        result3 = emotion_detector("I feel disgusted just hearing this")
        self.assertEqual(result3, 'disgust')

        result4 = emotion_detector("I feel sad about this")
        self.assertEqual(result4, 'sadness')

        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5, 'fear')


if __name__ == "__main__":
    unittest.main(verbosity=2)
