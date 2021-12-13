// use std::{
//     io::{self, Read},
// };

use std::io;
use std::io::Read;

pub fn p1() {
    let values = parse_input();
    let total = values.len();
    let mut ones: [u32; 12] = [0; 12];
    let mask: [u32; 12] = [
        0b100000000000,
        0b010000000000,
        0b001000000000,
        0b000100000000,
        0b000010000000,
        0b000001000000,
        0b000000100000,
        0b000000010000,
        0b000000001000,
        0b000000000100,
        0b000000000010,
        0b000000000001,
    ];
    for v in values {
        for i in 0..12 {
            if v & mask[i] != 0 {
                ones[i] += 1;
            }
        }
    }
    let mut gamma: i32 = 0;
    let mut epsilon: i32 = 0;
    for i in 0..12 {
        if ones[i] > (total as u32/ 2) {
            gamma |= mask[i] as i32;
        } else {
            epsilon |= mask[i] as i32;
        }
    }
    println!("{:012b} {:012b}", gamma, epsilon);
    println!("{} x {} = {}", gamma, epsilon, gamma*epsilon);
}

fn parse_input() -> Vec<u32> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).expect("fail on read input");
    let bnum = input.lines().map(
        |n| u32::from_str_radix(n, 2)
    ).collect::<Result<Vec<_>, _>>();
    return bnum.unwrap();
}