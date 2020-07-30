Bridge
================
Bridge is a structural design pattern that lets you split a large class or a set of related classes into two separate hierarchies - abstraction and implementation - which can be developed independently.

## Usage
- Use the pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).
- Use the pattern when you need to extend a class in several independent dimensions.
- Use the pattern if you need to be able to switch implementations at runtime

## Structure
![Structure](static/structure.png?raw=true)