# LearningJourney

**LearningJourney** is an iOS app that helps you track your daily learning streaks for a specific topic. The app allows you to log learned days, freeze days when needed, and monitor your streak status—whether it is ongoing, completed, or expired.

---

## Features

1. **Daily Streak Tracking**  
   - Mark a day as "Learned".  
   - Mark a day as "Freezed" with a maximum limit based on the selected streak duration.  
   - Automatically recalculates the streak when days are added or removed.

2. **Streak States**  
   - **Normal:** Days accumulate regularly.  
   - **Completed:** All required days for the selected duration (Week, Month, Year) are completed.  
   - **Expired:** The last logged day is older than 32 hours.

3. **User Interface**  
   - **MainView**:  
     - Displays a `CalendarCard` showing logged days.  
     - Buttons for **Pencil** (edit goal) and **Calendar** (view calendar).  
     - Buttons to log today as Learned or Freezed.  
   - **NewGoalView**:  
     - Allows setting a new **Learning Topic**.  
     - Select the learning duration (Week / Month / Year).  
     - Resets the streak when changing the goal or duration.

4. **Extensions & Helpers**  
   - Generates fake dates for testing (`Calendar.generateDates(forLastNDays:)`).  
   - Design helpers like `glassEffect()` and Gradients for buttons and cards.

---

## Setup & Running

1. Open the project in Xcode (recommended version: Xcode 15+).  
2. Make sure the **iOS Deployment Target** is set appropriately (e.g., iOS 17).  
3. Build and run the app on a **Simulator** or a physical device.  
4. Use **SwiftUI Previews** to test different streak scenarios:

```swift
// Example: Completed streak for a week
let completedManager = StreakViewModel(
    mockLearned: Set(Calendar.current.generateDates(forLastNDays: 7)),
    learningTopic: "Math",
    duration: .week
)

MainView(manager: completedManager)
