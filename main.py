import datetime
import json
from time import ctime
import os


class BlogPOst:
    date = ctime()

    def __init__(self, title=None, author=None, content=None, tags=None, date=None, post_details=None):
        if post_details is None:
            post_details = []
        self.title = title
        self.author = author
        self.content = content
        self.tags = tags
        self.date = date
        self.file_name = "post.json"
        self.post_details = self.load_file()

    def save_file(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.post_details, file, indent=4)

    def load_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def add_posts(self):
        while True:
            self.title = input("Enter the title of your post: ").lower()
            self.author = input("Enter the author: ").lower()
            if not self.title or not self.author:
                print("Title and Author cannot be empty")
                continue
            if self.title == 'o' or self.author == "o":
                print("Returning to main menu....")
                return

            while True:
                self.content = input("Enter post contents: ")
                if len(self.content) <= 20:
                    print("content cannot be less than 20 characters")
                    continue
                break

            self.tags = input("Enter posts tags separated by space if they are more than one eg: (Python Django CNN "
                              "War etc").split()

            self.post_details.append({
                "title": self.title,
                "author": self.author,
                "content": self.content,
                "tags": self.tags,
                "date_created": datetime.datetime.now().isoformat()
            })
            break

        for post in self.post_details:
            print(f"{post['title']} - {post['author']} - {post['content']} - {post['tags']} - {post['date_created']}")

        self.save_file()

    def view_all_post(self):
        sorted_post = sorted(self.post_details, key=lambda post: post['date_created'], reverse=True)


        print(f"{'Title:':<10} {'Author':<10} {'content':<50} {'Tags':<40} {'Time':<10}")
        for post in sorted_post:
            print(f"{post['title']:<10} {post['author']:<10} {post['content']:<50} {', '.join(post['tags']):<40} {post['date_created']:<10} \n")

    def single_post(self):
        pass

    def edit_post(self):

        find_input = input("Find the post you wish to replace by its title: ").strip().lower()
        found = False

        for post in self.post_details:
            if post['title'].lower() == find_input:
                print("\nEnter new values or 'N' to skip updating a field.\n")
                replace_title = input("Enter new title or N to skip: ").strip()
                replace_author = input("Enter new author or N to skip: ").strip()
                while True:
                    replace_content = input("Enter new content or N to skip: ").strip()
                    if len(self.content) <= 20:
                        print("content cannot be less than 20 characters")
                        continue
                    break


                replace_tag = input("Enter new tag or N to skip: ").split()

                if replace_title.lower() != "n":
                    post['title'] = replace_title
                if replace_author.lower() != "n":
                    post['author'] = replace_author
                if replace_content.lower() != "n":
                    post['content'] = replace_content
                if not (len(replace_tag) == 1 and replace_tag[0].lower() == 'n'):
                    post['tags'] = replace_tag

                post["date_created"]: datetime.datetime.now().isoformat()


                print("\nPost edited successfully.\n")
                self.save_file()
                found = True
                break  # stop looping once found

        if not found:
            print(f"\nPost titled '{find_input}' not found.\n")

    def delete_post(self):
        delete_input = input("Enter the title of post you wish to delete: ").strip().lower()
        for i, post in enumerate(self.post_details):
            if delete_input in post['title']:
                del self.post_details[i]
                self.save_file()
                print(f"{delete_input} was removed")
                break
        else:
            print(f"{delete_input} not found")
    def search_post_by_tag_author(self):
        search_item_input = input("Enter the title or tag of a post: ").strip().lower()
        for post in self.post_details:
            if search_item_input in post['title'] or search_item_input in post['tags']:
                print(post)
                break
        else:
            print("post not found")

class RunBlog(BlogPOst):
    def run_blog(self):
        try:
            while True:
                print("---- Blog Post Manager ----")
                print("1. Add Post")
                print("2. Search posts by tag or author ")
                print("3. Delete Post")
                print("4. View all Post")
                print("5. View single post")
                print("6. Edit Post")
                print("7. Exit")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    print("---------- Add New Blog Post ----------")
                    self.add_posts()
                elif choice == "2":
                    print("---------- Search Posts By tag or Author ----------")
                    self.search_post_by_tag_author()
                elif choice == "3":
                    print("---------- Delete Post ----------")
                    self.delete_post()
                elif choice == "4":
                    print("---------- View All Posts ----------")
                    self.view_all_post()
                elif choice == "5":
                    print("---------- Single Post ----------")
                    self.single_post()
                elif choice == "6":
                    print("---------- Edit Post ----------")
                    self.edit_post()
                elif choice == "7":
                    print("Exiting... Goodbye!")
                    break
                else:
                    print("Invalid choice. Try again.\n")
        except KeyboardInterrupt:
            print("\n  Blog Post Manager safely Ended \n")


runblog = RunBlog()
runblog.run_blog()
