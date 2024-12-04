
import cv2
import mediapipe as mp
import math

class HandGestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.gestures = {}
        self._initialize_gestures()

    def _initialize_gestures(self):
        # Define a large set of gestures
         self.gestures = {
            "Palma Abierta": self._is_open_palm,
            "Puno Cerrado": self._is_closed_fist,
            "Senalando": self._is_pointing,
            "Victoria": self._is_victory,
            "Pulgar Arriba": self._is_thumbs_up,
            "Pulgar Abajo": self._is_thumbs_down,
            "Senal de OK": self._is_ok_sign,
            "Rock and Roll": self._is_rock_on,
            "Pellizco": self._is_pinch,
            "Pistola": self._is_gun,
            "Saludo Vulcano": self._is_vulcan_salute,
            "Corazon con Dedos": self._is_finger_heart,
            "Tres Dedos": self._is_three_count,
            "Cuatro Dedos": self._is_four_count,
            "Mano Italiana": self._is_italian_hand,
            "Llamame": self._is_call_me,
            "Hang Loose": self._is_hang_loose,
            "Dedos Cruzados": self._is_finger_crossed,
            "Puno Levantado": self._is_raised_fist,
            "Choque de Punos": self._is_fist_bump,
        }

    def _get_angle(self, p1, p2, p3):
        radians = math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x)
        angle = abs(radians * 180.0 / math.pi)
        if angle > 180.0:
            angle = 360 - angle
        return angle

    def _get_distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

    def _is_finger_bent(self, finger_mcp, finger_pip, finger_dip, finger_tip, landmarks):
        angle = self._get_angle(landmarks[finger_mcp], landmarks[finger_pip], landmarks[finger_tip])
        return angle < 160  # Consider finger bent if angle is less than 160 degrees

    def _is_open_palm(self, landmarks):
        return all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 5, 9, 13, 17])

    def _is_closed_fist(self, landmarks):
        return all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 5, 9, 13, 17])

    def _is_pointing(self, landmarks):
        return (not self._is_finger_bent(5, 6, 7, 8, landmarks) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 9, 13, 17]))

    def _is_victory(self, landmarks):
        return (not self._is_finger_bent(5, 6, 7, 8, landmarks) and
                not self._is_finger_bent(9, 10, 11, 12, landmarks) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 13, 17]))

    def _is_thumbs_up(self, landmarks):
        return (not self._is_finger_bent(1, 2, 3, 4, landmarks) and
                landmarks[4].y < landmarks[3].y and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9, 13, 17]))

    def _is_thumbs_down(self, landmarks):
        return (not self._is_finger_bent(1, 2, 3, 4, landmarks) and
                landmarks[4].y > landmarks[3].y and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9, 13, 17]))

    def _is_ok_sign(self, landmarks):
        return (self._get_distance(landmarks[4], landmarks[8]) < 0.05 and
                all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [9, 13, 17]))

    def _is_rock_on(self, landmarks):
        return (not self._is_finger_bent(5, 6, 7, 8, landmarks) and
                not self._is_finger_bent(17, 18, 19, 20, landmarks) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 9, 13]))

    def _is_pinch(self, landmarks):
        return (self._get_distance(landmarks[4], landmarks[8]) < 0.05 and
                all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [9, 13, 17]))

    def _is_gun(self, landmarks):
        return (not self._is_finger_bent(5, 6, 7, 8, landmarks) and
                not self._is_finger_bent(1, 2, 3, 4, landmarks) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [9, 13, 17]))

    def _is_vulcan_salute(self, landmarks):
        return (not self._is_finger_bent(5, 6, 7, 8, landmarks) and
                not self._is_finger_bent(9, 10, 11, 12, landmarks) and
                not self._is_finger_bent(17, 18, 19, 20, landmarks) and
                self._is_finger_bent(13, 14, 15, 16, landmarks))

    def _is_finger_heart(self, landmarks):
        return (self._get_distance(landmarks[4], landmarks[8]) < 0.05 and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [9, 13, 17]))

    def _is_three_count(self, landmarks):
        return (all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9, 13]) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 17]))

    def _is_four_count(self, landmarks):
        return (all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9, 13, 17]) and
                self._is_finger_bent(1, 2, 3, 4, landmarks))

    def _is_italian_hand(self, landmarks):
        return (all(self._get_distance(landmarks[i], landmarks[0]) < 0.1 for i in [4, 8, 12, 16, 20]) and
                all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 5, 9, 13, 17]))

    def _is_call_me(self, landmarks):
        return (not self._is_finger_bent(17, 18, 19, 20, landmarks) and
                not self._is_finger_bent(1, 2, 3, 4, landmarks) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9, 13]))

    def _is_hang_loose(self, landmarks):
        return (not self._is_finger_bent(1, 2, 3, 4, landmarks) and
                not self._is_finger_bent(17, 18, 19, 20, landmarks) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9, 13]))

    def _is_finger_crossed(self, landmarks):
        return (self._get_distance(landmarks[8], landmarks[12]) < 0.05 and
                all(not self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [5, 9]) and
                all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 13, 17]))

    def _is_raised_fist(self, landmarks):
        return (all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 5, 9, 13, 17]) and
                landmarks[0].y < landmarks[9].y)

    def _is_fist_bump(self, landmarks):
        return (all(self._is_finger_bent(i, i+1, i+2, i+3, landmarks) for i in [1, 5, 9, 13, 17]) and
                landmarks[0].y > landmarks[9].y)

    def detect_gesture(self, landmarks):
        for gesture, check_func in self.gestures.items():
            if check_func(landmarks):
                return gesture
        return "Unknown"

    def process_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        detected_gestures = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
                gesture = self.detect_gesture(hand_landmarks.landmark)
                detected_gestures.append(gesture)

        return frame, detected_gestures

def main():
    cap = cv2.VideoCapture(0)
    detector = HandGestureDetector()

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        frame, gestures = detector.process_frame(frame)

        for i, gesture in enumerate(gestures):
            cv2.putText(frame, f"Gesture {i+1}: {gesture}", (10, 30 + i * 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Advanced Hand Gesture Detection', frame)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

