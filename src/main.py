# Import custom classes
from model.model import RocketModel
from view.view import RocketView
from controller.controller import RocketController

# This conditional makes sure your code only runs when the script is executed directly
# and not when it's imported as a module in another script.
if __name__ == "__main__":
    # Create an instance of the Model. This is where you'll manage your sensor data
    # and database interactions.
    model = RocketModel()

    # Create an instance of the View. The View is responsible for presenting data to the user.
    # Since you only need console output, this can start as simple print statements.
    view = RocketView()

    # Create an instance of the Controller, passing in the model and view.
    # The Controller will handle user inputs and update the View based on data from the Model.
    controller = RocketController(model, view)

    # You might want to have a loop here for continuous updates.
    # If you need to perform tasks at a set interval, you can use a time.sleep() call.
    # If the script is meant to run indefinitely, consider handling exit conditions properly.
    try:
        while True:
            # This function call tells the controller to update the View with new data.
            controller.update_view()

            # If your sensors update frequently, you could add a sleep here.
            # For example, time.sleep(1) would pause the loop for 1 second before continuing.
            # This is important to prevent your loop from consuming too much CPU by running as fast as possible.
    except KeyboardInterrupt:
        # This block allows the user to stop the loop with a keyboard interrupt (Ctrl+C).
        print("Shutting down the rocket controller.")
        # Here you could also add any necessary clean-up code to safely terminate the application.
