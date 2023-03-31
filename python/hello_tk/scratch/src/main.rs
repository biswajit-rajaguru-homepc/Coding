

pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
    let mut rs = Vec::new();
    let mut sum = 0;
    for num in nums {
        sum += num;
        rs.push(sum);

    }
    rs
}
fn main() {

    let nums = vec![1, 2, 3, 4];

    println!("{:?}", running_sum(nums))

}
