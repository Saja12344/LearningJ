//
//  StreakView 2.swift
//  LearningJ
//
//  Created by saja khalid on 06/05/1447 AH.
//


import SwiftUI

struct StreakView: View {
    @StateObject private var viewModel = StreakViewModel()

    var body: some View {
        VStack(spacing: 16) {
            Text("Current Streak")
                .font(.headline)

            
            Text("\(viewModel.streakDays) 🔥")
                .font(.system(size: 48, weight: .bold, design: .rounded))

            Text("Freezes used: \(viewModel.freezesUsed)")

            HStack {
                Button("Mark Learned") { viewModel.markAsLearned() }
                Button("Freeze Day") { viewModel.toggleFreeze() }
                Button("Unfreeze") { viewModel.unfreezeDay() }
            }
            .buttonStyle(.bordered)
        }
        .padding()
    }
}
