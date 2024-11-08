//
//  SonarSwiftSampleTests.swift
//  SonarSwiftSampleTests
//
//  Created by Vignesh Jeyaraj on 08/11/24.
//

import XCTest
@testable import SonarSwiftSample

final class SonarSwiftSampleTests: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }
    
    func testAdd() {
        let sample = SonarSwiftSample()
        
        XCTAssertEqual(sample.add(2, 3), 5)
    }
}
