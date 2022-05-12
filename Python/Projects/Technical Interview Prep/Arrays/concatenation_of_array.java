class concatenation_of_array {
   public void getConcatenation(int[] nums) {
      int[] result = new int[nums.length * 2];
      for (int i = 0; i < nums.length; i++)
         result[i + nums.length] = result[i] = nums[i];
      System.out.print(result);
   }
   
   public static void main(String args[]) {
      concatenation_of_array ans = new concatenation_of_array();
      
      int[] nums = {1,2,1};
      System.out.print(ans.getConcatenation(nums));
   }
}

