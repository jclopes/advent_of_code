use std::env;

mod d03;

fn main() {
    if let Some(arg) = env::args().nth(1) {
        match arg.as_str() {
            "3" => d03::p1(),
            _ => eprintln!("not implemented or invalid argument: {}", arg),
        };
    } else {
        eprintln!("missing day argument");
    }
}