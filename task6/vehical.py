from datetime import datetime, timedelta

class Vehicle:
    """Base class for all vehicles."""
    def __init__(self, vehicle_id, brand, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"{self.vehicle_id}: {self.brand} {self.model} - ₹{self.daily_rate}/day ({status})"


class Car(Vehicle):
    """Car subclass."""
    def __init__(self, vehicle_id, brand, model, daily_rate, seats):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.seats = seats

    def __str__(self):
        return super().__str__() + f" | Seats: {self.seats}"


class Bike(Vehicle):
    """Bike subclass."""
    def __init__(self, vehicle_id, brand, model, daily_rate, engine_cc):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.engine_cc = engine_cc

    def __str__(self):
        return super().__str__() + f" | Engine: {self.engine_cc}cc"


class Rental:
    """Handles rental transactions."""
    def __init__(self, vehicle, customer_name, rental_days):
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.rental_days = rental_days
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=rental_days)
        self.total_cost = self.rental_days * self.vehicle.daily_rate

    def __str__(self):
        return (f"Rental: {self.customer_name} rented {self.vehicle.brand} {self.vehicle.model} "
                f"for {self.rental_days} days. Total: ₹{self.total_cost}")


class RentalSystem:
    """Main rental system."""
    def __init__(self):
        self.vehicles = []
        self.rentals = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_available_vehicles(self):
        print("\nAvailable Vehicles:")
        for v in self.vehicles:
            if v.is_available:
                print(v)

    def rent_vehicle(self, vehicle_id, customer_name, rental_days):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id and v.is_available:
                rental = Rental(v, customer_name, rental_days)
                self.rentals.append(rental)
                v.is_available = False
                print("\n✅ Rental Successful!")
                print(rental)
                return
        print("\n❌ Vehicle not available or invalid ID.")

    def return_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id and not v.is_available:
                v.is_available = True
                print(f"\n✅ Vehicle {vehicle_id} returned successfully.")
                return
        print("\n❌ Invalid vehicle ID or vehicle is already available.")


# ------------------ DEMO ------------------
if __name__ == "__main__":
    system = RentalSystem()

    # Adding vehicles
    system.add_vehicle(Car("C101", "Toyota", "Innova", 2500, 7))
    system.add_vehicle(Car("C102", "Hyundai", "i20", 1500, 5))
    system.add_vehicle(Bike("B201", "Yamaha", "R15", 800, 155))
    system.add_vehicle(Bike("B202", "Royal Enfield", "Classic 350", 1000, 350))

    # Display available vehicles
    system.display_available_vehicles()

    # Rent a vehicle
    system.rent_vehicle("C101", "Arun Kumar", 3)

    # Display available vehicles after renting
    system.display_available_vehicles()

    # Return a vehicle
    system.return_vehicle("C101")

    # Display available vehicles after return
    system.display_available_vehicles()