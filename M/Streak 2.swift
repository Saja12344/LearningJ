//
//  Streak 2.swift
//  LearningJ
//
//  Created by saja khalid on 06/05/1447 AH.
//


import Foundation

struct Streak: Codable, Equatable {
    var learnedDates: Set<Date> = []
    var freezedDates: Set<Date> = []
    var streakDays: Int = 0
    var freezesUsed: Int = 0
    
    var lastLoggedDate: Date? = nil
}
