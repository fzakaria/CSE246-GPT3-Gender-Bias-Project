import pandas as pd

if __name__ == '__main__':
    
    resume_df = pd.read_csv('./raw_resume.csv')
    female_names = pd.read_csv('./names/female-only-names.csv')
    male_names = pd.read_csv('./names/male-only-names.csv')

    N = 100

    # name, category, resume content
    m_name_c = male_names.iloc[:, 0][:N]
    f_name_c = female_names.iloc[:, 0][:N]
    resume_category = resume_df.iloc[:, 0][: N]
    resume_content = resume_df.iloc[:, 1][: N]

    f_df = pd.DataFrame(data = {
        'NAME': f_name_c,
        'CATEGORY': resume_category,
        'RESUME': resume_content
    })

    m_df = pd.DataFrame(data = {
        'NAME': m_name_c,
        'CATEGORY': resume_category,
        'RESUME': resume_content
    })

    total_dataset = pd.concat([f_df, m_df], ignore_index=True)
    # remove some special char like . ; * â¢
    total_dataset['RESUME'] = total_dataset['RESUME'].str.replace('\\n|\\r|;|â||¢|\*', '')
    
    # remove stop words
    stop_words = []
    sw_file = open('stop_words')
    [stop_words.append(w.replace('\n', '')) for w in sw_file.readlines()]
    print(stop_words)
    total_dataset['RESUME'] = total_dataset['RESUME'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))

    print(total_dataset)
    total_dataset.to_csv("./resume.csv", )