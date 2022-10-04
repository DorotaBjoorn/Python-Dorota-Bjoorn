import numpy as np

def trigonometric_identity(angle: float) -> float:
    """Calculates trig identinty
    
    raaram:
    angle: angle in radians
    
    return: trigonometic one
    """

    print("Running trigonometic_identinty()")
    return (np.cos(angle) ** 2 + np.sin(angle) **2)

if __name__ == "__main__":                                  # kan därför importera denna fil från andra utan att koden körs
    print("Running directly from module2.py")
    print(trigonometric_identity(42))
else:                                                       # vanligtvis har man inte else satsen, här för att visa vad som händer
    print("You have imported me")                           # i detta fall blir __name__ module2 så den körs från main