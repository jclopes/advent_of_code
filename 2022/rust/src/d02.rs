use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

pub fn p1() -> i32 {
    let a: u32 = 'A'.into();
    let x: u32 = 'X'.into();
    let input = read_input();

    let mut score_sum = 0;
    for l in input {
        let round = l.as_bytes();
        let player_a = i32::try_from(round[0] as u32 - a).unwrap();
        let player_b = i32::try_from(round[2] as u32 - x).unwrap();
        score_sum += round_score(player_a, player_b);
    }
    return score_sum;
}

pub fn p2() -> i32 {
    let a: u32 = 'A'.into();
    let input = read_input();

    let mut score_sum = 0;
    for l in input {
        let round = l.as_bytes();
        let player_a = i32::try_from(round[0] as u32 - a).unwrap();
        let player_b = choose_play(player_a, round[2] as char);
        score_sum += round_score(player_a, player_b);
    }
    return score_sum;
}

fn choose_play(player_a: i32, action: char) -> i32 {
    let mut player_b = match action as char {
        'X' => player_a - 1,    // lose
        'Y' => player_a,        // draw
        'Z' => player_a + 1,    // win
        _ => -23,
    };
    if player_b < 0 {
        player_b += 3;
    }
    if player_b > 2 {
        player_b -= 3;
    }
    return player_b;
}

fn round_score(player_a: i32, player_b: i32) -> i32 {
    let mut score = player_b + 1;

    score += match player_b - player_a {
        0 => 3,
        -1 => 0,
        -2 => 6,
        1 => 6,
        2 => 0,
        _ => 0,

    };
    return score;
}

fn read_input() -> Vec<String> {
    let input = lines_from_file("../input/02.txt").unwrap();

    let mut res: Vec<String> = Vec::new();
    for l in input {
        res.push(l.trim().to_string());
    }
    return res;
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}
