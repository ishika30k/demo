from insert_data import my_user_entry
from insert_data import my_user_skin_info
from insert_data import my_ingredient_info
from insert_data import my_feedback_table


def main():
	n=int(input("Enter no. of entries u want : "))
	my_user_entry(n)
	my_user_skin_info(n)
	my_ingredient_info(n)
	my_feedback_table(n)

main()


