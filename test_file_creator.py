test_file = input("Enter path to your test file: ").strip()

with open(test_file, mode='w') as f:
    lines = ('id{}row\n'.format(i) for i in range(600))
    f.writelines(lines)
