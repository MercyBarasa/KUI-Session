
      <div class="modal-body" >
        <div class="container py-5">
        <div class="row">
            <div class="col-md-5 mx-auto bCapacityg-white shadow border p-4 rounded">
                <h2 class="text-center fw-bold mb-3">SMS Sender</h2>

                <form method="POST" Action="SaveCarRental.php" enctype="multipart/form-data">
              
              <div class="form-group mb-3">
                  <label for="exampleFormControlInput1">Add Car Model </label>
                  <input type="string" class="form-control" id="ItemName" name="model"  placeholder="enter car model">
                   
              </div>
             <div class="form-group mb-3">
                  <label for="exampleFormControlInput1">Price Per Day</label>
                  <input type="string" class="form-control" id="Price" name="hire_cost"  placeholder="Enter hire cost">
                   
              </div>

               <div class="form-group mb-3">
                  <label for="exampleFormControlInput1">Seating Capacity</label>
                  <input type="string" class="form-control" id="Price" name="capacity"  placeholder=" enter Seating ">
              </div>

               <div class="form-group mb-3">
                  <label for="exampleFormControlInput1">Car Description</label>
                  <input type="string" class="form-control" id="Price" name="description"  placeholder="Car Description">
              </div> 

              <div class="form-group mb-3">
                  <label for="exampleFormControlInput1">Upload Item Image</label>
                  <input type="file" name="image" class="form-control" >
              </div>
              
            <div>
              <button type="submit"  name="submit" class="btn btn-primary">Submit</button>
          </div>
            </form>
               
            </div>
        </div>
    </div>
      </div>
      </center>
     <!--  <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div> -->
    
</div>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/js/bootstrap.min.js'></script>
</body>
</html>
